<template>
    <div id="body">
        <bk-form :label-width="200" :model="form">
            <bk-form-item label="起始日期" :required="true" :property="'start_time'">
                <bk-date-picker placeholder="选择日期" behavior="simplicity" v-model="form.start_time" :disabled="modifying" />
                <div class="warn" v-show="ilegalTime">起始日期应在截止日期之前</div>
            </bk-form-item>
            <bk-form-item label="截止日期" :required="true" :property="'end_time'">
                <bk-date-picker placeholder="选择日期" behavior="simplicity" v-model="form.end_time" :disabled="modifying" />
                <div class="warn" v-show="ilegalTime">起始日期应在截止日期之前</div>
            </bk-form-item>
            <bk-form-item label="计划招募人数" :required="true" :property="'recruit_num'">
                <bk-input v-model.number="form.recruit_num" placeholder="输入人数" style="width: 40%" :disabled="modifying" />
            </bk-form-item>
            <bk-form-item label="面试轮数" :required="true" :property="'interview_rounds'">
                <bk-input v-model.number="form.interview_rounds" placeholder="输入人数" style="width: 40%" :disabled="modifying" />
            </bk-form-item>
            <bk-form-item v-show="emptyItems">
                <div class="warn">有一处或多处必填信息未填写</div>
            </bk-form-item>
            <bk-form-item v-show="submitted">
                <div class="success">已保存</div>
            </bk-form-item>
            <bk-form-item id="buttons">
                <bk-button theme="primary" :disabled="modifying" @click="submit">保存</bk-button>
                <bk-button theme="default" hover-theme="warning" @click="modifying = false">编辑</bk-button>
            </bk-form-item>
        </bk-form>
        <div v-show="submitted">{{form}}</div>
    </div>
</template>

<script>
    export default {
        name: 'manageRecruit',

        data () {
            return {
                form: {
                    club_id: 114514,
                    recruit_num: '',
                    start_time: '',
                    end_time: '',
                    interview_rounds: ''
                },
                emptyItems: false,
                ilegalTime: false,
                modifying: true,
                submitted: false
            }
        },

        created () {
            this.getRecruitInfo()
        },

        methods: {
            submit () {
                this.emptyItems = false
                this.ilegalTime = false
                for (const item in this.form) {
                    if (!this.form[item]) {
                        this.emptyItems = true
                        return
                    }
                }
                const dateStart = new Date(this.form.start_time)
                const dateEnd = new Date(this.form.end_time)
                if (dateStart >= dateEnd) {
                    this.ilegalTime = true
                } else {
                    this.modifying = true
                    this.submitted = true
                }
            },
            async getRecruitInfo () {
                const { data } = await this.$store.dispatch('getRecruitInfo')
                this.form = data.form
            }
        }
    }
</script>

<style scoped>
#body {
    margin: 20px 5% 20px 5%;
    padding: 10px 10px 10px 10px;
}
#buttons {
    display: flex;
    flex-flow: column nowrap;
    justify-content: space-around;
}
.warn {
    font-size: 5px;
    color: red;
}
.success {
    font-size: 5px;
    color: deepskyblue;
}
</style>
