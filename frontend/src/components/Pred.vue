<template>
  <div v-if="msprediction" key="loading"></div>
</template>

<script>
import {mapState} from 'vuex';
export default {
  name: 'msprediction',
  computed: mapState(['loading', 'complex']),
};
</script>

<style>

</style>