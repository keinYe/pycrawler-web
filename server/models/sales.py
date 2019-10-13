# -*- coding:utf-8 -*-
import logging
from server.database import CRUDMixin
from server.module import db
import datetime
from server.template_filter import format_date
# from pycrawler.agent.models import Agent, Contact

class Agent(db.Model, CRUDMixin):
    ''' 代理商 '''
    __tablename__ = 'agent'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    name = db.Column(db.String(200), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    tel = db.Column(db.String(20))
    fax = db.Column(db.String(20))
    contact = db.relationship('Contact', backref='agent')

    def to_json(self):
        return {
            'id': self.id,
            'date': self.date,
            'name': self.name,
            'address': self.address,
            'tel': self.tel,
            'fax': self.fax,
            'contact': [x.to_json() for x in self.contact]
        }

class Contact(db.Model, CRUDMixin):
    ''' 联系人 '''
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    tel = db.Column(db.String(20))

    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'))

    def to_json(self):
        return {
            'id': self.id,
            'date': self.date,
            'name': self.name,
            'address': self.address,
            'tel': self.tel
        }

class Note(db.Model, CRUDMixin):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    deliverynote_id = db.Column(db.Integer, db.ForeignKey('deliverynote.id'))

    def to_json(self):
        return {
            'id': self.id,
            'model': self.model,
            'quantity': self.quantity,
        }

class DeliveryNote(db.Model, CRUDMixin):
    __tablename__ = 'deliverynote'å
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nmuber = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    salesrecord_number = db.Column(db.String(20), nullable=False)
    out_receipt_number = db.Column(db.String(20), nullable=False)
    note = db.relationship('Note', backref='deliverynote.id')

    def to_json(slef):
        return {
            'id': self.id,
            'number': self.number,
            'date': format_date(self.date),
            'salesrecord_number': self.salesrecord_number,
            'out_receipt_number': self.out_receipt_number,
            'note': [x.to_json() for x in self.note]
        }

class SalesRecord(db.Model, CRUDMixin):
    __tablename__ = 'salesrecord'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nmuber = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    model = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    applicant = db.Column(db.String(50), nullable=False)
    # 代理商名称
    agent_name = db.Column(db.String(200))
    # 收货人信息
    contact_name = db.Column(db.String(200), nullable=False)
    contact_address = db.Column(db.String(200), nullable=False)
    contact_tel = db.Column(db.String(20), nullable=False)
    # 操作员
    operator = db.Column(db.String(20), nullable=False)
    remarks = db.Column(db.String(200))

    def to_json(self):
        return {
            'id': self.id,
            'number': self.number,
            'date': format_date(self.date),
            'model': self.model,
            'quantity': self.quantity,
            'applicant': self.applicant,
            'agent_name': self.agent_name,
            'contact_name': self.contact_name,
            'contact_address': self.contact_address,
            'contact_tel': self.contact_tel,
            'operator': self.operator,
            'remarks': self.remarks
        }
