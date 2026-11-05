import json,math
from .common import number,integer,identifier,unique_ids
def run(d):
 rows=d['nodes'];unique_ids(rows)
 if len(rows)>1000:raise ValueError('nodes')
 nodes={r['id']:r for r in rows};pending=set(nodes);causes={};order=[]
 for r in rows:
  if not isinstance(r['depends_on'],list)or any(x not in nodes for x in r['depends_on']):raise ValueError('dependency')
  if r['status']not in ['valid','invalid','unknown']:raise ValueError('status')
 while pending:
  ready=sorted(k for k in pending if all(x in causes for x in nodes[k]['depends_on']))
  if not ready:raise ValueError('cycle')
  for k in ready:
   r=nodes[k];why=set().union(*(causes[x]for x in r['depends_on']))
   if r['status']!='valid':why.add(k)
   causes[k]=why;pending.remove(k);order.append(k)
 return dict(topological_order=order,results=[dict(id=k,usable=not causes[k],blocking_roots=sorted(causes[k]),own_status=nodes[k]['status'])for k in order],minimal_invalidation_sources=sorted(k for k,r in nodes.items()if r['status']!='valid'))
