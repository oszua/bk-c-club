<template>
    <div>
        <h2>{{ tmpl.name }}</h2>
        <span class="desc">{{ tmpl.desc }}</span>
        <bk-form :model="flowInputs" form-type="vertical">
            <bk-form-item v-for="item in tmpl.form" :key="item.key">
                <h3 class="form-item-label">{{ item.name }}</h3>
                <span class="desc">{{ item.desc }}</span>
                <component :is="getComp(item.type)" :ikey="item.key" :props="item.props" v-model="flowInputs[item.key]" />
            </bk-form-item>
        </bk-form>
        <div>{{ flowInputs }}</div>
    </div>
</template>

<script>
    export default {
        name: 'formRender',
        props: {
            /**
             * tmpl
             * {
             *     "name": "通知插件",
             *     "desc": "使用这个插件可以给其他人发送邮件",
             *     "form": [
             *         {
             *             // type: "textarea" | etc.
             *             "type": "textarea",
             *             "name": "通知模板",
             *             "key": "notify_tmpl",
             *             "desc": "姓名使用${name}代替",
             *             "props": {
             *                 "placeholder": "欢迎${name}同学报名本社团！"
             *             }
             *         }
             *     ]
             * }
             */
            tmpl: Object
        },
        data () {
            return {
                map: {
                    'textarea': {
                        props: {
                            props: Object,
                            ikey: String,
                            value: String
                        },
                        computed: {
                            _value: {
                                get () {
                                    return this.value
                                },
                                set (val) {
                                    this.$emit('input', val)
                                }
                            }
                        },
                        template: `
                            <bk-input type="textarea" :placeholder="props.placeholder" :name="ikey" v-model="_value"/>`
                    }
                },
                flowInputs: {}
            }
        },
        methods: {
            getComp (type) {
                return this.map[type]
            }
        }
    }
</script>

<style scoped>
.desc {
    font-size: 12px;
}

.form-item-label {
    margin-bottom: 0;
}
</style>
