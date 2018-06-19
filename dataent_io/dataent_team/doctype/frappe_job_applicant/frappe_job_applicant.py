# Copyright (c) 2015, Dataent and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import dataent
from dataent.model.document import Document

class DataentJobApplicant(Document):
	def before_insert(self):
		'''don't accept if applying in 30 days'''
		if dataent.db.sql('''select name from `tabDataent Job Applicant`
			where email=%s and creation > adddate(curdate(), interval -30 day)''', self.email):
			dataent.throw('We have already recived your application. You can apply again after 30 days!')
