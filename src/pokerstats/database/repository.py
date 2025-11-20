from sqlalchemy.orm import Session
from sqlalchemy import or_
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
        ids_trans_processados = set()

        for item in lista_consolidados:
            r = item.resumo 
            
            id_transacao = item.dados_financeiros.id_referencia if item.dados_financeiros else None
            id_hh = item.dados_hh.id_hh if item.dados_hh else None

            if id_hh and id_hh in ids_hh_processados: continue
            if id_transacao and id_transacao in ids_trans_processados: continue

            if id_hh: ids_hh_processados.add(id_hh)
            if id_transacao: ids_trans_processados.add(id_transacao)

            db_transacao = None
            criteria = []
            if id_transacao: criteria.append(TransacaoDB.id_transacao == id_transacao)
            if id_hh: criteria.append(TransacaoDB.id_hh == id_hh)

            if criteria:
                db_transacao = self.db.query(TransacaoDB).filter(or_(*criteria)).first()

            try:
                                
                if db_transacao:
                    if id_hh and not db_transacao.id_hh: db_transacao.id_hh = id_hh
                    if id_transacao and not db_transacao.id_transacao: db_transacao.id_transacao = id_transacao
                    
                    db_transacao.status = r['Status']
                    db_transacao.nome_torneio = r['Torneio']
                    
                    if item.dados_financeiros:
                        db_transacao.buy_in = r['BuyIn']
                        db_transacao.premio = r['Premio']
                        db_transacao.data_inicio = r['Data']
                    
                    if db_transacao.resultado:
                        db_transacao.resultado.lucro = r['Lucro'] 
                        db_transacao.resultado.roi = r['ROI']     
                    else:
                        db_transacao.resultado = ResultadoDB(lucro=r['Lucro'], roi=r['ROI'])

                    count_atualizados += 1
                else:
                    nova_transacao = TransacaoDB(
                        id_transacao=id_transacao,
                        id_hh=id_hh,
                        data_inicio=r['Data'],
                        nome_torneio=r['Torneio'],
                        buy_in=r['BuyIn'],
                        premio=r['Premio'],
                        status=r['Status'],
                        resultado=ResultadoDB(lucro=r['Lucro'], roi=r['ROI'])
                    )
                    self.db.add(nova_transacao)
                    count_novos += 1
                
                self.db.flush()

            except IntegrityError:
                self.db.rollback()
                continue
            except Exception as e:
                self.db.rollback()
                print(f"Erro item {id_hh}: {e}")
                continue
        
        try:
            self.db.commit()
        except Exception:
            self.db.rollback()

        return count_novos, count_atualizados

    def listar_todos(self):
        from sqlalchemy.orm import joinedload
        return self.db.query(TransacaoDB).options(joinedload(TransacaoDB.resultado)).order_by(TransacaoDB.data_inicio.desc()).all()