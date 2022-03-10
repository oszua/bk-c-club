/**
 * @file mock index module
 * @author DomineCore
 */

import chalk from 'chalk'

import { sleep } from './util'

export async function response (getArgs, postArgs, req) {
    console.log(chalk.cyan('req', req.method))
    console.log(chalk.cyan('getArgs', JSON.stringify(getArgs, null, 0)))
    console.log(chalk.cyan('postArgs', JSON.stringify(postArgs, null, 0)))
    console.log()
    const invoke = getArgs.invoke
    if (invoke === 'getUserInfo') {
        return {
            code: 0,
            data: {
                id: '1234567890',
                username: 'admin',
                timestamp: +new Date
            },
            message: 'ok'
        }
    } else if (invoke === 'enterExample1') {
        const delay = getArgs.delay
        await sleep(delay)
        return {
            // http status code, 后端返回的数据没有这个字段，这里模拟这个字段是为了在 mock 时更灵活的自定义 http status code，
            // 同时热更新即改变 http status code 后无需重启服务，这个字段的处理参见 build/ajax-middleware.js
            // statusCode: 401,
            code: 0,
            data: {
                msg: `我是 enterExample1 请求返回的数据。本请求需耗时 ${delay} ms`
            },
            message: 'ok'
        }
    } else if (invoke === 'enterExample2') {
        const delay = postArgs.delay
        await sleep(delay)
        return {
            // http status code, 后端返回的数据没有这个字段，这里模拟这个字段是为了在 mock 时更灵活的自定义 http status code，
            // 同时热更新即改变 http status code 后无需重启服务，这个字段的处理参见 build/ajax-middleware.js
            // statusCode: 401,
            code: 0,
            data: {
                msg: `我是 enterExample2 请求返回的数据。本请求需耗时 ${delay} ms`
            },
            message: 'ok'
        }
    } else if (invoke === 'btn1') {
        const delay = getArgs.delay
        await sleep(delay)
        return {
            // http status code, 后端返回的数据没有这个字段，这里模拟这个字段是为了在 mock 时更灵活的自定义 http status code，
            // 同时热更新即改变 http status code 后无需重启服务，这个字段的处理参见 build/ajax-middleware.js
            // statusCode: 401,
            code: 0,
            data: {
                msg: `我是 btn1 请求返回的数据。本请求需耗时 2000 ms. ${+new Date()}`
            },
            message: 'ok'
        }
    } else if (invoke === 'btn2') {
        const delay = getArgs.delay
        await sleep(delay)
        return {
            // http status code, 后端返回的数据没有这个字段，这里模拟这个字段是为了在 mock 时更灵活的自定义 http status code，
            // 同时热更新即改变 http status code 后无需重启服务，这个字段的处理参见 build/ajax-middleware.js
            // statusCode: 401,
            code: 0,
            data: {
                msg: `我是 btn2 请求返回的数据。本请求需耗时 2000 ms. ${+new Date()}`
            },
            message: 'ok'
        }
    } else if (invoke === 'del') {
        return {
            code: 0,
            data: {
                msg: `我是 del 请求返回的数据。请求参数为 ${postArgs.time}`
            },
            message: 'ok'
        }
    } else if (invoke === 'getFlow') {
        return {
            code: 0,
            data: {
                flow: [
                    {
                        "name": "节点name",
                        "description": "节点描述",
                        "component_code": "插件code",
                        "version": "插件版本",
                        "inputs": [
                            {
                                "key":"notify_tmpl",
                                "value":"欢迎{name}参加一轮面试",
                            }
                        ]
                    },
                    {
                        "name": "节点name",
                        "description": "节点描述",
                        "component_code": "插件code",
                        "version": "插件版本",
                        "inputs": [

                        ]
                    }
                ]
            },
            message: 'ok'
        }
    } else if (invoke === 'getRecruitInfo') {
        return {
            code: 0,
            data: {
                form: {
                    club_id: 114514,
                    recruit_num: '50',
                    start_time: '',
                    end_time: '',
                    interview_rounds: ''
                },
                message: 'ok'
            }
        }
    }
    return {
        code: 0,
        data: {}
    }
}
