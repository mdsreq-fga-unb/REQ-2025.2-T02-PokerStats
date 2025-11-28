from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .config import Base

class TransacaoDB(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    
    id_transacao = Column(String, unique=True, nullable=True, index=True)
    id_hh = Column(String, unique=True, nullable=True, index=True)
    data_inicio = Column(DateTime)
    nome_torneio = Column(String)
    buy_in = Column(Float, default=0.0)
    premio = Column(Float, default=0.0)
    status = Column(String)
    
    resultado = relationship("ResultadoDB", back_populates="transacao", uselist=False, cascade="all, delete-orphan")

class ResultadoDB(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    transacao_id = Column(Integer, ForeignKey("transacoes.id"), unique=True, nullable=False)
    lucro = Column(Float, default=0.0)
    roi = Column(Float, default=0.0)
    ITM = Column(Float, default=0.0)
    
    transacao = relationship("TransacaoDB", back_populates="resultado")