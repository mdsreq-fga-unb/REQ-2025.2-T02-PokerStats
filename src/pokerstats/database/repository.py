from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, func, delete
from sqlalchemy.exc import IntegrityError
from .schemas import TransacaoDB, ResultadoDB
from .config import Base, engine
from ..core.models import TorneioConsolidado

Base.metadata.create_all(bind=engine)

class TorneioRepository:
    def __init__(self, db: Session):
        self.db = db

    def salvar_consolidacao(self, lista_consolidados: list[TorneioConsolidado]):
        count_novos = 0
        count_atualizados = 0
        ids_hh_processados = set()

        for item in lista_consolidados:
            r = item.resumo 
            
            id_transacao = item.dados_financeiros.id_referencia if item.dados_financeiros else None
            id_hh = item.dados_hh.id_hh if item.dados_hh else None

            if id_hh and id_hh in ids_hh_processados: 
                continue
            
            if id_hh: ids_hh_processados.add(id_hh)

            db_transacao = None
            criteria = []
            if id_transacao: criteria.append(TransacaoDB.id_transacao == id_transacao)
            if id_hh: criteria.append(TransacaoDB.id_hh == id_hh)

            if criteria:
                db_transacao = self.db.query(TransacaoDB).filter(or_(*criteria)).first()

            try:
                novo_buyin = float(r['BuyIn'] or 0.0)
                novo_premio = float(r['Premio'] or 0.0)
                
                buyin_final = novo_buyin
                premio_final = novo_premio

                if db_transacao:
                    if item.dados_financeiros:
                        buyin_atual = float(db_transacao.buy_in or 0.0)
                        premio_atual = float(db_transacao.premio or 0.0)
                        
                        buyin_final = max(buyin_atual, novo_buyin)
                        premio_final = max(premio_atual, novo_premio)
                        
                        db_transacao.buy_in = buyin_final
                        db_transacao.premio = premio_final
                        
                        if r['Data'] and db_transacao.data_inicio and r['Data'] < db_transacao.data_inicio:
                            db_transacao.data_inicio = r['Data']
                        elif r['Data'] and not db_transacao.data_inicio:
                            db_transacao.data_inicio = r['Data']

                    if id_hh and not db_transacao.id_hh: db_transacao.id_hh = id_hh
                    if id_transacao and not db_transacao.id_transacao: db_transacao.id_transacao = id_transacao
                    
                    db_transacao.status = r['Status']
                    if r['Torneio'] != "Desconhecido":
                        db_transacao.nome_torneio = r['Torneio']
                    
                    lucro_final = premio_final - buyin_final
                    roi_final = ((premio_final - buyin_final) / buyin_final * 100) if buyin_final > 0 else 0.0

                    if db_transacao.resultado:
                        db_transacao.resultado.lucro = lucro_final
                        db_transacao.resultado.roi = roi_final
                    else:
                        db_transacao.resultado = ResultadoDB(lucro=lucro_final, roi=roi_final)

                    count_atualizados += 1
                else:
                    lucro_final = premio_final - buyin_final
                    roi_final = ((premio_final - buyin_final) / buyin_final * 100) if buyin_final > 0 else 0.0
                    
                    nova_transacao = TransacaoDB(
                        id_transacao=id_transacao,
                        id_hh=id_hh,
                        data_inicio=r['Data'],
                        nome_torneio=r['Torneio'],
                        buy_in=buyin_final,
                        premio=premio_final,
                        status=r['Status'],
                        resultado=ResultadoDB(lucro=lucro_final, roi=roi_final)
                    )
                    self.db.add(nova_transacao)
                    count_novos += 1
                
                self.db.flush()

            except IntegrityError:
                self.db.rollback()
                continue
            except Exception as e:
                self.db.rollback()
                print(f"Erro no item {id_transacao}: {e}")
                continue
        
        try:
            self.db.commit()
        except Exception:
            self.db.rollback()

        return count_novos, count_atualizados

    def listar_todos(self):
        return self.db.query(TransacaoDB).options(joinedload(TransacaoDB.resultado)).order_by(TransacaoDB.data_inicio.desc()).all()

    def buscar_por_id(self, db_id: int):
        return self.db.query(TransacaoDB).options(joinedload(TransacaoDB.resultado)).filter(TransacaoDB.id == db_id).first()

    def contar_transacoes_existentes(self, lista_ids: list[str]) -> int:
        if not lista_ids: return 0
        return self.db.query(TransacaoDB).filter(TransacaoDB.id_transacao.in_(lista_ids)).count()

    def obter_somas_totais(self):
        return self.db.query(func.sum(TransacaoDB.buy_in), func.sum(TransacaoDB.premio)).first()

    def listar_dados_analiticos(self):
        return self.db.query(TransacaoDB.nome_torneio, TransacaoDB.buy_in, TransacaoDB.premio).all()

    def listar_transacoes_sem_hh(self):
        return self.db.query(TransacaoDB).filter(or_(TransacaoDB.id_hh == None, TransacaoDB.id_hh == "")).all()

    def deletar_transacao(self, transacao_id: int):
        try:
            item = self.db.query(TransacaoDB).get(transacao_id)
            if item:
                self.db.delete(item)
                self.db.commit()
                return True
            return False
        except Exception as e:
            self.db.rollback()
            raise e

    def atualizar_transacao(self, transacao_id: int, dados: dict):
        try:
            item = self.db.query(TransacaoDB).get(transacao_id)
            if not item: return False

            item.nome_torneio = dados.get('nome', item.nome_torneio)
            item.buy_in = float(dados.get('buy_in', item.buy_in))
            item.premio = float(dados.get('premio', item.premio))
            
            lucro = item.premio - item.buy_in
            roi = ((item.premio - item.buy_in) / item.buy_in * 100) if item.buy_in > 0 else 0.0

            if item.resultado:
                item.resultado.lucro = lucro
                item.resultado.roi = roi
            else:
                item.resultado = ResultadoDB(lucro=lucro, roi=roi)

            self.db.commit()
            self.db.refresh(item)
            return item
        except Exception as e:
            self.db.rollback()
            raise e

    def deletar_em_lote(self, lista_ids: list[int]):
        try:
            stmt = delete(TransacaoDB).where(TransacaoDB.id.in_(lista_ids))
            self.db.execute(stmt)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e

    def limpar_banco(self):
        """
        Deleta explicitamente ResultadoDB depois TransacaoDB para evitar orfãos
        e problemas de integridade.
        """
        try:
            self.db.query(ResultadoDB).delete()
            
            self.db.query(TransacaoDB).delete()
            
            self.db.commit()
            
            self.db.expire_all()
            
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Erro ao limpar banco: {e}")
            raise e