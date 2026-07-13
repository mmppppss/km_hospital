from odoo import http
from odoo.http import request


class KmHospital(http.Controller):

    _patient_fields = {'name', 'phone', 'email', 'age', 'gender', 'address'}
    _appointment_fields = {'name', 'patient_id', 'checkup_date', 'appointed_doctor_id', 'status'}

    @http.route('/patient_webform', type='http', auth='user', website=True)
    def patient_webform(self, **kw):
        return request.render('km_hospital.create_patient', {})

    @http.route('/create/webpatient', type="http", auth="user", website=True)
    def create_webpatient(self, **kw):
        vals = {k: v for k, v in kw.items() if k in self._patient_fields and v}
        request.env['kmhospital.patient'].sudo().create(vals)
        return request.render("km_hospital.patient_thanks", {})

    @http.route('/patient_view', type='http', auth='public', website=True)
    def view_patient_web(self, **kw):
        patients = request.env['kmhospital.patient'].sudo().search([])
        return request.render('km_hospital.view_patient', {
            'patients': patients
        })

    @http.route('/appointment_webform', type='http', auth='user', website=True)
    def appointment_webform(self, **kw):
        patient_rec = request.env['kmhospital.patient'].sudo().search([])
        doctor_rec = request.env['kmhospital.doctor'].sudo().search([])
        return request.render('km_hospital.create_appointment', {
            'patient_rec': patient_rec,
            'doctor_rec': doctor_rec
        })

    @http.route('/create/webappointment', type="http", auth="user", website=True)
    def create_webappointment(self, **kw):
        vals = {k: v for k, v in kw.items() if k in self._appointment_fields and v}
        request.env['kmhospital.appointment'].sudo().create(vals)
        return request.render("km_hospital.appointment_thanks", {})