#### 流程系统调用说明
1. 创建流程模板
    ```python
    from engine.flowtmpl.models import FlowTmpl
    FlowTmpl.objects.create(......)
    # tree字段需要符合flow.tmpl.valid下的rule

2. 流程相关
    ```python
    from engine.flow.dispatcher import FlowDispathcer
    # 1. 流程实例化
    pipeline = FlowDispathcer.build_pipeline(flowtmpl.tree, student_id, club_id)
    # 2. 启动流程
    FlowDispatcher.run(pipeline)
    # 3. 撤销流程
    FlowDispatcher.revoke(piepline["id"])
    # 4. 跳过流程某节点
    FlowDispatcher.skip_node(node_id)
    # 5. 获取流程执行状态
    FlowDispatcher.get_flow_states(pipeline["id"])

3. 更加底层的使用方法（bamboo-engine原生调用）

    戳👉https://github.com/TencentBlueKing/bamboo-engine/
