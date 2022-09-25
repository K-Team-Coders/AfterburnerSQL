<template>
  <div v-if="loading" key="loading">
    <div class="text-center">
      <div class="spinner-border" role="status" style="width: 3rem; height: 3rem;">
        <span class="visually-hidden">Загрузка...</span>
      </div>
    </div>
  </div>
  <div v-else-if="M1" key="M1.probs, M2.data, M3.compl"><p>Предсказание выполнения запроса по количеству операторов: {{Math.round(M1.data.result)}}ms </p> 
    <p>Предсказание выполнения запроса по телу запроса:{{Math.round(M2.data.result)}} ms</p> </div>
  <div v-else key="not-found">Не найдено</div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  computed: mapState(['loading', 'M1', 'M2', 'M3']),
};
</script>

<style>

</style>