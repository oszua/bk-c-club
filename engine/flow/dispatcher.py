from logging import root
from bamboo_engine import builder, api
from bamboo_engine.builder import (
    EmptyStartEvent,
    ServiceActivity,
    EmptyEndEvent,
    Var
)
from pipeline.eri.runtime import BambooDjangoRuntime

from engine.flow.context import FlowContext


RUNTIME = BambooDjangoRuntime()


class FlowDispatcher():
    @classmethod    
    def build_pipeline(self, tree, student_id, club_id):
        """
        @summary:使用流程模板tree、学生id、社团id构造一条flow
        """
        # 编排流程
        start = EmptyStartEvent()
        end = EmptyEndEvent()
        node = start
        for component in tree:
            act = ServiceActivity(component_code=component["component_code"])
            # 填充inputs
            for item in component["inputs"]:
                value = Var(type=Var.PLAIN, value=item["value"])
                setattr(act.component.inputs, item["key"], value)
            node = node.extend(act)
        node.extend(end)
        # 设置数据上下文
        context = FlowContext.get_context(student_id, club_id)
        pipeline = builder.build_tree(start, data=context)
        return pipeline
    
    @classmethod
    def run(self, pipeline):
        """
        @summay: 启动flow.pipeline
        """
        api.run_pipeline(runtime=RUNTIME, pipeline=pipeline)

    @classmethod
    def revoke(self, pipeline_id):
        """
        @summay: 使用pipeline_id撤销pipeline
        """
        api.revoke_pipeline(runtime=RUNTIME, pipeline_id=pipeline_id)
    
    @classmethod
    def skip_node(self, node_id):
        """
        @summary: 跳过某节点
        """
        api.skip_node(runtime=RUNTIME, node_id=node_id)

    @classmethod
    def get_flow_states(self, pipeline_id):
        """
        @summary: 使用pipeline_id获取pipeline执行状态
        return data example:
        {
            'children': {
                u'377d513285963a40951eea983e62f899': {
                    'finish_time': '2019-03-28 13:48:43',
                    'id': u'377d513285963a40951eea983e62f899',
                    'loop': 1L,
                    'name': u'act_4',
                    'retry': 0L,
                    'skip': False,
                    'start_time': '2019-03-28 13:48:43',
                    'state': 'FINISHED'
                },
                u'45d24e4595dd32b3ab65feddc73a75c3': {
                    'finish_time': '2019-03-28 13:48:43',
                    'id': u'45d24e4595dd32b3ab65feddc73a75c3',
                    'loop': 1L,
                    'name': u'act_1',
                    'retry': 0L,
                    'skip': False,
                    'start_time': '2019-03-28 13:48:43',
                    'state': 'FINISHED'
                },
                u'a4ee2f04cbdb3e87a5563f2907d5c42f': {
                    'finish_time': '2019-03-28 13:48:43',
                    'id': u'a4ee2f04cbdb3e87a5563f2907d5c42f',
                    'loop': 1L,
                    'name': u'[act_2] or [act_3 and act_4]',
                    'retry': 0L,
                    'skip': False,
                    'start_time': '2019-03-28 13:48:43',
                    'state': 'FINISHED'
                },
                u'bacfee844f313c7285b0e3f83f187745': {
                    'finish_time': '2019-03-28 13:48:43',
                    'id': u'bacfee844f313c7285b0e3f83f187745',
                    'loop': 1L,
                    'name': u'act_3',
                    'retry': 0L,
                    'skip': False,
                    'start_time': '2019-03-28 13:48:43',
                    'state': 'FINISHED'
                },
                ...
            }
        }
        """
        return api.get_pipeline_states(runtime=RUNTIME, root_id=pipeline_id)

