<template>
    <div :class="systemCls" class="monitor-navigation">
        <bk-navigation
            :default-open="true"
            :navigation-type="'left-right'"
            :need-menu="true"
            @toggle="handleToggle">
            <template slot="side-header">
                <div class="debug logo">Logo</div>
                <div class="debug">蓝鲸社团报名管理系统</div>
            </template>
            <template slot="header">
                <div class="header-container">
                    <!-- pageHead -->
                    <div class="page-title-container">
                        <span class="header-title-icon" @click="handleRouterBack">
                            <svg class="icon" style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4756"><path d="M416 480h320v64H416l96 96-48 48-176-176 176-176 48 48-96 96z" p-id="4757"></path></svg>
                        </span>
                        <span class="header-title">{{nav.list.filter(value => value.id === $route.name)[0].name}}</span>
                    </div>
                    <!-- userInfo -->
                    <div>userInfo</div>
                </div>
            </template>
            <template slot="menu">
                <bk-navigation-menu
                    ref="menu"
                    @select="handleSelect"
                    :default-active="nav.id"
                    :toggle-active="nav.toggle">
                    <bk-navigation-menu-item
                        v-for="item in nav.list"
                        :key="item.id"
                        :has-child="item.children && !!item.children.length"
                        v-bind="item">
                        <span>{{ item.name }}</span>
                    </bk-navigation-menu-item>
                </bk-navigation-menu>
            </template>
            <div class="monitor-navigation-content">
                <main v-bkloading="{ isLoading: mainContentLoading, opacity: 1 }" class="main-content">
                    <router-view v-show="!mainContentLoading" :key="routerKey" />
                </main>
            </div>
            <template slot="footer">
                <div class="monitor-navigation-footer">
                    Copyright © 2022-{{ new Date().getFullYear() }} Tencent BlueKing. All Rights Reserved. 腾讯蓝鲸 版权所有
                </div>
            </template>
        </bk-navigation>
        <app-auth ref="bkAuth"></app-auth>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex'

    import { bus } from '@/common/bus'

    export default {
        name: 'monitor-navigation',
        data () {
            return {
                routerKey: +new Date(),
                systemCls: 'mac',
                nav: {
                    list: [
                        {
                            id: 'editFlow',
                            icon: 'icon-pipeline',
                            name: '招募流程',
                            pathName: 'editFlow'
                        },
                        {
                            id: 'manageRecruit',
                            icon: 'icon-monitors-cog',
                            name: '招募管理',
                            pathName: 'manageRecruit'
                        },
                        {
                            id: 'clubInfo',
                            icon: 'icon-panel-permission',
                            name: '社团信息',
                            pathName: 'clubInfo'
                        },
                        {
                            id: 'checkinData',
                            icon: 'icon-bar-chart',
                            name: '报名信息',
                            pathName: 'checkinData'
                        }
                    ],
                    id: 'editFlow',
                    toggle: true,
                    title: '蓝鲸社团报名管理系统'
                }
            }
        },
        computed: {
            ...mapGetters(['mainContentLoading'])
        },
        created () {
            const platform = window.navigator.platform.toLowerCase()
            if (platform.indexOf('win') === 0) {
                this.systemCls = 'win'
            }
        },
        mounted () {
            const self = this
            bus.$on('show-login-modal', data => {
                self.$refs.bkAuth.showLoginModal(data)
            })
            bus.$on('close-login-modal', () => {
                self.$refs.bkAuth.hideLoginModal()
                setTimeout(() => {
                    window.location.reload()
                }, 0)
            })
        },
        updated () {
            this.nav.id = this.$route.name
        },
        methods: {
            handleSelect (id, item) {
                this.nav.id = id
                this.$router.push({
                    name: item.pathName
                })
            },
            handleToggle (v) {
                this.nav.toggle = v
            },
            handleRouterBack () {
                this.$router.back()
            }
        }
    }
</script>

<style lang="postcss">
@import './css/reset.css';
@import './css/app.css';

.debug {
    color: #ff6666;
}

.header-container {
    display: flex;
    width: 100%;
    justify-content: space-between;
}

.header-title {
    cursor: default;
}

.header-title-icon{
    width:28px;
    height:28px;
    font-size:28px;
    color:#3A84FF;
    cursor: pointer;
}

.monitor-navigation-header {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    overflow: hidden;
    height: 100%;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    font-size: 14px;

    .header-nav {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        padding: 0;
        margin: 0;
    }

    .header-nav-item {
        list-style: none;
        height: 50px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        margin-right: 40px;
        color: #96A2B9;
        min-width: 56px;

        &.item-active {
            color: #fff !important;
        }

        &:hover {
            cursor: pointer;
            color: #d3d9e4;
        }
    }

    .header-title {
        color: #63656E;
        font-size: 16px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        margin-left: -6px;
    }

    .header-title-icon {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        width: 28px;
        height: 28px;
        font-size: 28px;
        color: #3a84ff;
        cursor: pointer;
    }

    .header-select {
        width: 240px;
        margin-left: auto;
        margin-right: 34px;
        border: none;
        background: #252f43;
        color: #d3d9e4;
        -webkit-box-shadow: none;
        box-shadow: none;
    }

    .header-mind {
        color: #768197;
        font-size: 16px;
        position: relative;
        height: 32px;
        width: 32px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        justify-content: center;
        margin-right: 8px;

        &:hover {
            background: -webkit-gradient(linear, right top, left top, from(rgba(37, 48, 71, 1)), to(rgba(38, 50, 71, 1)));
            background: linear-gradient(270deg, rgba(37, 48, 71, 1) 0%, rgba(38, 50, 71, 1) 100%);
            border-radius: 100%;
            cursor: pointer;
            color: #d3d9e4;
        }

        .lang-icon {
            font-size: 20px;
        }
    }

    .header-mind-mark {
        position: absolute;
        right: 8px;
        top: 8px;
        height: 7px;
        width: 7px;
        border: 1px solid #27334C;
        background-color: #EA3636;
        border-radius: 100%
    }

    .header-help {
        color: #768197;
        font-size: 16px;
        position: relative;
        height: 32px;
        width: 32px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        justify-content: center;
        margin-right: 8px;

        &:hover {
            background: -webkit-gradient(linear, right top, left top, from(rgba(37, 48, 71, 1)), to(rgba(38, 50, 71, 1)));
            background: linear-gradient(270deg, rgba(37, 48, 71, 1) 0%, rgba(38, 50, 71, 1) 100%);
            border-radius: 100%;
            cursor: pointer;
            color: #d3d9e4;
        }
    }

    .header-user {
        height: 100%;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        justify-content: center;
        color: #96A2B9;
        margin-left: 8px;

        &:hover {
            cursor: pointer;
            color: #d3d9e4;
        }

        .bk-icon {
            margin-left: 5px;
            font-size: 12px;
        }
    }
}

.monitor-navigation-content {
    padding: 5px 15px 15px 15px;
    font-size: 14px;
    color: #737987;
    height: calc(100% - 84px);
    background: #FFFFFF;
    -webkit-box-shadow: 0px 2px 4px 0px rgba(25, 25, 41, 0.05);
    box-shadow: 0px 2px 4px 0px rgba(25, 25, 41, 0.05);
    border-radius: 2px;
    border: 1px solid rgba(220, 222, 229, 1);

    .main-content {
        min-height: 600px;
    }
}

.monitor-navigation-footer {
    height: 52px;
    width: 100%;
    margin: 32px 0 0;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
    border-top: 1px solid #dcdee5;
    color: #63656e;
    font-size: 12px;
}

.monitor-navigation-message {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    width: 360px;
    background-color: #ffffff;
    border: 1px solid #e2e2e2;
    border-radius: 2px;
    -webkit-box-shadow: 0px 3px 4px 0px rgba(64, 112, 203, 0.06);
    box-shadow: 0px 3px 4px 0px rgba(64, 112, 203, 0.06);
    color: #979ba5;
    font-size: 12px;

    .message-title {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 48px;
        flex: 0 0 48px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        color: #313238;
        font-size: 14px;
        padding: 0 20px;
        margin: 0;
        border-bottom: 1px solid #f0f1f5;
    }

    .message-list {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        max-height: 450px;
        overflow: auto;
        margin: 0;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
        -ms-flex-direction: column;
        flex-direction: column;
        padding: 0;
    }

    .message-list-item {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        width: 100%;
        padding: 0 20px;

        &:hover {
            cursor: pointer;
            background: #F0F1F5;
        }

        .item-message {
            padding: 13px 0;
            line-height: 16px;
            min-height: 42px;
            -webkit-box-flex: 1;
            -ms-flex: 1;
            flex: 1;
            -ms-flex-wrap: wrap;
            flex-wrap: wrap;
            color: #63656E;
        }

        .item-date {
            padding: 13px 0;
            margin-left: 16px;
            color: #979BA5;
        }
    }

    .message-footer {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 42px;
        flex: 0 0 42px;
        border-top: 1px solid #f0f1f5;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        justify-content: center;
        color: #3a84ff;
    }
}

.monitor-navigation-nav {
    width: 150px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    background: #FFFFFF;
    border: 1px solid #E2E2E2;
    -webkit-box-shadow: 0px 3px 4px 0px rgba(64, 112, 203, 0.06);
    box-shadow: 0px 3px 4px 0px rgba(64, 112, 203, 0.06);
    padding: 6px 0;
    margin: 0;
    color: #63656E;

    .nav-item {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 32px;
        flex: 0 0 32px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        padding: 0 16px;
        list-style: none;

        &:hover {
            color: #3A84FF;
            cursor: pointer;
            background-color: #F0F1F5;
        }

        .lang-icon {
            font-size: 20px;
            margin-right: 6px;
        }
    }
}

.monitor-navigation-admin {
    width: 170px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    background: #FFFFFF;
    border: 1px solid #E2E2E2;
    -webkit-box-shadow: 0px 3px 4px 0px rgba(64, 112, 203, 0.06);
    box-shadow: 0px 3px 4px 0px rgba(64, 112, 203, 0.06);
    padding: 6px 0;
    margin: 0;
    color: #63656E;

    .nav-item {
        -webkit-box-flex: 0;
        -ms-flex: 0 0 32px;
        flex: 0 0 32px;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        padding: 0 16px;
        list-style: none;

        &:hover {
            color: #3A84FF;
            cursor: pointer;
            background-color: #F0F1F5;
        }

        .lang-icon {
            font-size: 20px;
            margin-right: 6px;
        }
    }
}

.tippy-popper .tippy-tooltip.navigation-message-theme {
    padding: 0;
    border-radius: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
}
</style>
