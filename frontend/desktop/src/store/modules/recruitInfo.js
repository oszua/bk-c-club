/**
 * @file recruitInfo store
 * @author AutumnSaury
 */

import http from '@/api'

export default {
    namespace: true,
    state: {
        form: {}
    },
    mutations: {
    },
    actions: {
        getRecruitInfo (context) {
            const mockUrl = `?${AJAX_MOCK_PARAM}=index&invoke=getRecruitInfo`
            return http.get(mockUrl, {}, {})
        }
    }
}
