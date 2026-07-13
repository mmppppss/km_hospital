from odoo.exceptions import ValidationError
from odoo import api, fields, models, _


class AppointmentReportWizard(models.TransientModel):
    _name = "kmhospital.appointment.report.wizard"
    _description = "Print Appointment Wizard"

    date_from = fields.Datetime(string='Date from')
    date_to = fields.Datetime(string='Date to')
    patient_id = fields.Many2one('kmhospital.patient', string="Patient", required=True)

    def action_print_report(self):
        if self.date_from and self.date_to and self.date_from > self.date_to:
            raise ValidationError(_("Date from must be previous than date to."))

        domain = []
        if self.patient_id:
            domain += [('patient_id', '=', self.patient_id.id)]
        if self.date_from:
            domain += [('checkup_date', '>=', self.date_from)]
        if self.date_to:
            domain += [('checkup_date', '<=', self.date_to)]

        appointments = self.env['kmhospital.appointment'].search_read(domain)

        data = {
            'form_data': {
                'patient_id': self.patient_id.id,
                'date_from': str(self.date_from) if self.date_from else '',
                'date_to': str(self.date_to) if self.date_to else '',
            },
            'appointments': appointments
        }
        return self.env.ref('km_hospital.action_report_appointment_card').report_action(self, data=data)
