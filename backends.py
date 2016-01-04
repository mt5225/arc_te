from __future__ import absolute_import
from celery.backends import mongodb
from celery import states
from datetime import datetime
import json
import urllib2

__FLOWER_URL__ = "http://localhost:5555/api/task/info/"


def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z


class CustomMongoBackend(mongodb.MongoBackend):
    """
    This backend removes the default storing of result data as Binary.
    """
    def _store_result(self, task_id, result, status,
                      traceback=None, request=None, **kwargs):
        """Store return value and status of an executed task."""
        data = json.load(urllib2.urlopen(__FLOWER_URL__ + task_id))  # get more details from flower
        meta = {'_id': task_id,
                'status': status,
                'result': result,
                'date_done': datetime.utcnow(),
                'task': request.task
                }
        record = merge_two_dicts(meta, data)
        self.collection.save(record)
        return result

    def _save_group(self, group_id, result):
        """Save the group result."""
        meta = {'_id': group_id,
                'result': self.encode(result),
                'date_done': datetime.utcnow()}
        self.collection.save(meta)
        return result

    def _get_task_meta_for(self, task_id):
        """Get task metadata for a task by id."""
        obj = self.collection.find_one({'_id': task_id})
        if not obj:
            return {'status': states.PENDING, 'result': None}
        meta = {
            'task_id': obj['_id'],
            'status': obj['status'],
            'result': obj['result'],
            'date_done': obj['date_done'],
            'traceback': self.decode(obj['traceback']),
            'children': self.decode(obj['children']),
        }
        return meta
