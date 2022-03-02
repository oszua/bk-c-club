/**
 * @file flow store
 * @author LiuMingxun
 */
import http from '@/api'

export default {
    namespace: true,
    state: {
        flow: []
    },
    mutations: {
    },
    actions: {
        getFlow (state) {
            const mockUrl = `?${AJAX_MOCK_PARAM}=index&invoke=getFlow`
            return http.get(mockUrl, {}, {})
        }
    }
}
