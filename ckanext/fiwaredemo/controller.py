import ckan.logic as logic
import ckan.model as model

from ckan.controllers.organization import OrganizationController
from ckan.common import c

NotFound = logic.NotFound
#check_access = logic.check_access

class FiwaredemoController(OrganizationController):

    def users(self, id):
        group_type = self._ensure_controller_matches_group_type(id)

        context = {'model': model, 'session': model.Session,
                   'user': c.user}

        try:
            data_dict = {'id': id}
            #check_access('group_edit_permissions', context, data_dict)
            c.members = self._action('member_list')(
                context, {'id': id, 'object_type': 'user'}
            )
            data_dict['include_datasets'] = False
            c.group_dict = self._action('group_show')(context, data_dict)
        except NotFound:
            abort(404, _('Group not found'))
        #except NotAuthorized:
        #    abort(403, _('User %r not authorized to edit members of %s') % (c.user, id))

        return self._render_template('organization/users.html', group_type)
