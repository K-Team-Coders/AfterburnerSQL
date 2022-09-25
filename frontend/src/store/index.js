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
      M1: 'null',
      M2: 'null',
      M3: 'null'
    },
  },
  getters: {

  },
  mutations: {
    [SET_SEARCH_QUERY]: (state, searchQuery) => state.searchQuery = searchQuery,
    [SET_PROBITY_RES]: (state, M1) => state.M1 = M1,
    [SET_COMPLEX_RES]: (state, M2) => state.M2 = M2,
    [SET_RESULT_RES]: (state, M3) => state.M3 = M3,
    [SET_LOADING]: (state, loading) => state.loading = loading,
    [RESET_SEARCH]: state => state.M1 = null,
    [RESET_SEARCH]: state => state.M2 = null,
    [RESET_SEARCH]: state => state.M3 = null,
    

  },
  actions: {
    setSearchQuery({commit}, searchQuery) {
      commit(SET_SEARCH_QUERY, searchQuery);
    },
    async search({commit, state}) {
      commit(SET_LOADING, true);
      try {
        const {data} = await axios.get(`http://127.0.0.1:8000/main/predict_query_time_execution/${state.searchQuery}/`);
        commit(SET_RESULT_RES, data);
        let probs = await axios.get(`http://127.0.0.1:8000/main/predict_query_time_execution_operators/${state.searchQuery}/`);
        commit(SET_PROBITY_RES, probs);
        let compl = await axios.get(`http://127.0.0.1:8000/main/predictQueryResponseTimeDesicionTree/${state.searchQuery}/`);
        commit(SET_COMPLEX_RES, compl);
        console.log(probs)
      } catch (e) {
        commit(RESET_SEARCH);
      }
      commit(SET_LOADING, false);
    
  }},
  modules: {

  }
})