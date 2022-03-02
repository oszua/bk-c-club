<template>
    <section>
        <header>
            <div>
                <bk-input behavior="simplicity" value="流程模板" />
            </div>
            <div>
                <bk-button type="primary">保存</bk-button>
            </div>
        </header>
        <section>
            <bk-card :show-head="false" class="flow-card">
                <div class="flow-item" v-for="(flowItem, index) in flow" :key="index">
                    <span>{{flowItem.name}}</span>
                </div>
            </bk-card>
        </section>
        <div>
            <form-render :tmpl="tmpl" />
        </div>
    </section>
</template>

<script>
    import FormRender from '../components/formRender'
    export default {
        name: 'editFlow',
        components: { FormRender },

        data () {
            return {
                flow: [],
                tmpl: {
                    'name': '通知插件',
                    'desc': '使用这个插件可以给其他人发送邮件',
                    'form': [
                        {
                            // type: "textarea" | etc.
                            'type': 'textarea',
                            'name': '通知模板',
                            'key': 'notify_tmpl',
                            'desc': '姓名使用${name}代替',
                            'props': {
                                'placeholder': '欢迎${name}同学报名本社团！'
                            }
                        },
                        {
                            // type: "textarea" | etc.
                            'type': 'textarea',
                            'name': '通知模板',
                            'key': 'others',
                            'desc': '姓名使用${name}代替',
                            'props': {
                                'placeholder': '欢迎${name}同学报名本社团！'
                            }
                        }
                    ]
                }
            }
        },
        mounted () {
            this.getFlow()
        },
        methods: {
            async getFlow () {
                const { data } = await this.$store.dispatch('getFlow')
                this.flow = data.flow
            }
        }
    }
</script>

<style scoped>
header {
    display: flex;
    padding-bottom: 4px;
    border-bottom: #ccc 1px solid;
    margin-bottom: 4px;
}

header * {
    display: inline-block;
}

.flow-card {
    width: 550px;
}

.flow-item {
    display: block;
    padding: 15px;
}
</style>
