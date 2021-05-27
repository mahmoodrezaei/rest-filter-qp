from rest_framework import filters as filt
import json
from .config import FILTER_TYPES
from rest_framework import serializers
class FilterParams(filt.BaseFilterBackend):



	def filter_queryset(self,request,queryset,view,*args,**kwargs):
		self_only=0
		filters = []


		if request.query_params.get('filters[]'):
			filters = self.optimize_parameters(filters=json.loads(request.query_params.get('filters[]')))




		index_self_only = next((index for (index,value) in enumerate(filters) if value['key'] == 'self_only'),None)
		if index_self_only != None:
			self_only = filters.pop(index_self_only)['value']
		if self_only:
			queryset = queryset.filter(user=request.user)


		for filter in filters:
				if FILTER_TYPES[filter['type']]['type'] == 'list':
					for key,value in enumerate(filter['key']):
						if FILTER_TYPES[filter['type']]['method']:
							queryset = queryset.filter(**{value:FILTER_TYPES[filter['type']]['method']()[key]})
							print(queryset)
						else:
							queryset = queryset.filter(**{value:filter['value'][key]})
				elif FILTER_TYPES[filter['type']]['method'] is not None:
					if FILTER_TYPES[filter['type']]['is_aggregate']:
						max_field = queryset.aggregate(
							maxfield=FILTER_TYPES[filter['type']]['method'](filter['key']))['maxfield']
						queryset = queryset.filter(**{filter['key']:max_field})
					else:
						queryset = queryset.filter(**{filter['key']:FILTER_TYPES[filter['type']]['method']()})
				elif FILTER_TYPES[filter['type']]['type'] == 'sort':
					queryset = queryset.order_by(filter['key'])
				else:
					queryset = queryset.filter(**{filter['key']:filter['value']})
		return queryset





	def optimize_parameters(self,filters):
		for filter in filters:
			if not filter['type'] in FILTER_TYPES.keys():
				raise serializers.ValidationError({'no_exist':
					{'message':'نوع فیلتر غیر مجاز است لطفا از لیست انتخاب کنید.',
					'fields':FILTER_TYPES.keys()
					}})
			if FILTER_TYPES[filter['type']]['extra_keys']:
				temp_key = filter['key']
				filter['key'] = []
				extra_keys = FILTER_TYPES[filter['type']]['extra_keys']
				if len(extra_keys) == 1 :
					filter['key'] = f'{temp_key}__{extra_keys[0]}'
				else:
					for extra_key in extra_keys:
						filter['key'].append(f'{temp_key}__{extra_key}')
		return filters