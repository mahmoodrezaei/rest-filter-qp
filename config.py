from django.db.models import Max,Min
from .methods import *

FILTER_TYPES = {
		'max':{
			'type' : 'int',
			'len' : 1,
			'extra_keys':[],
			'method' : Max,
			'is_aggregate':True
		},
		'min':{
			'type' : 'int',
			'len' : 1,
			'extra_keys':[],
			'method' : Min,
			'is_aggregate':True
		},
		'bwn':{
			'type' : 'list',
			'len' : 2,
			'extra_keys':['gte','lte'],
			'method' : None,
			'is_aggregate':False
		},
		'normal':{
			'type' : None,
			'len' : 1,
			'extra_keys':[],
			'method' : None,
			'is_aggregate':False
		},
		'today':{
			'type' : 'list',
			'len'  : 1,
			'extra_keys' : ['year','month','day'],
			'method' : this_day,
			'is_aggregate':False
		},
		'toweek' : {
			'type':'rang',
			'len' : 1,
			'extra_keys' : ['range'],
			'method' : this_week,
			'is_aggregate':False
		},
		'tomonth' : {
			'type' : 'list',
			'len' : 1,
			'extra_keys' : ['year','month'],
			'method' : this_month,
			'is_aggregate':False
		},
		'asc' : {
			'type' : 'sort',
			'len' : 1,
			'extra_keys' : [],
			'method' : None,
			'is_aggregate' : False
		},
		'desc' : {
			'type' : 'sort',
			'len' : 1,
			'extra_keys' : [],
			'method' : None,
			'is_aggregate' : False
		}
	}