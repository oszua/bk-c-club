from bamboo_engine.builder import Data,Var

class FlowContext():
    @classmethod
    def get_context(self, student_id, club_id):
        """
        将建立信息传递进流程上下文
        """
        context = Data()
        context.inputs["student_id"] = Var(type=Var.PLAIN, value=student_id)
        context.inputs["club_id"] = Var(type=Var.PLAIN, value=club_id)
        return context
