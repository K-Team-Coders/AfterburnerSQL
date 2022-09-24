import { createStore } from 'vuex'
import axios from 'axios'

const SET_SEARCH_QUERY = 'SET_SEARCH_QUERY';
const SET_LOADING = 'SET_LOADING';
const SET_RESULT_RES = 'SET_RESULT_RES';
const RESET_SEARCH = 'RESET_SEARCH';
const SET_PROBITY_RES = 'SET_PROBILITY_RES';
const SET_COMPLEX_RES = 'SET_COMPLEX_RES';

export default createStore({
  state: {
    state: {
      searchQuery: '',
      loading: false,
      tnved: 'null',
      probility: 'null',
      complex: 'null'
    },
  },
  getters: {

  },
  mutations: {
    [SET_SEARCH_QUERY]: (state, searchQuery) => state.searchQuery = searchQuery,
    [SET_PROBITY_RES]: (state, probility) => state.probility = probility,
    [SET_LOADING]: (state, loading) => state.loading = loading,
    [RESET_SEARCH]: state => state.tnved = null,

    

  },
  actions: {
    setSearchQuery({commit}, searchQuery) {
      commit(SET_SEARCH_QUERY, searchQuery);
    },
    async search({commit, state}) {
      commit(SET_LOADING, true);
      try {
        const {data} = await axios.get(`http://127.0.0.1:8000/predict_query_time_execution/${state.searchQuery}/`);
        commit(SET_RESULT_RES, data);
      } catch (e) {
        commit(RESET_SEARCH);
      }
      commit(SET_LOADING, false);
    
  }},
  modules: {

  }
})