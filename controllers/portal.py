from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class CoffeePortal(CustomerPortal):

    @http.route('/my/machine/<int:machine_id>', type='http', auth='user', website=True)
    def view_machine(self, machine_id):
        machine = request.env['coffee.machine'].sudo().browse(machine_id)

        # Ensure machine exists and belongs to current user
        if not machine.exists() or machine.owner_id.id != request.env.user.partner_id.id:
            return request.redirect('/my')

        return request.render('Machine_Maintiance_system.machine_detail_portal', {
            'machine': machine,
        })

    @http.route('/my/complaint/new/<int:machine_id>', type='http', auth='user', website=True, methods=['GET', 'POST'])
    def submit_complaint(self, machine_id, **post):
        machine = request.env['coffee.machine'].sudo().browse(machine_id)

        if not machine.exists() or machine.owner_id.id != request.env.user.partner_id.id:
            return request.redirect('/my')

        if request.httprequest.method == 'POST':
            message = post.get('message')
            if message:
                request.env['coffee.complaint'].sudo().create({
                    'machine_id': machine.id,
                    'user_id': request.env.user.id,
                    'message': message,
                })
                return request.redirect('/my/machine/%s' % machine.id)

        return request.render('Machine_Maintiance_system.portal_submit_complaint', {
            'machine': machine,
        })
    @http.route('/my/machines', type='http', auth='user', website=True)
    def portal_my_machines(self):
        machines = request.env['coffee.machine'].sudo().search([
            ('owner_id', '=', request.env.user.partner_id.id)
        ])
        return request.render('Machine_Maintiance_system.portal_my_machines_page', {
            'machines': machines,
        })