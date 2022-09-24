<template>
  <Scatter
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
    :tables1="tables1"
    :into="into"
    :join="join"
  />
</template>

<script>
import HomeView from '@/views/HomeView.vue' 
import { Scatter } from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  PointElement,
  LinearScale
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  PointElement,
  LinearScale
)

export default {
  name: 'ScatterChart',
  components: {
    Scatter
  },
  props: {
    chartId: {
      type: String,
      default: 'scatter-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    },
    tables1: '',
    join: '',
    from: '',
    into: '',
    
  },
  data() {
    return {
      chartData: {
        datasets: [
          {
            label: 'SELECT',
            fill: false,
            borderColor: '#887BB5',
            backgroundColor: '#4528A4',
            data: [ {1.2, 4.5}
            ]
          },
          {
            label: 'INTO',
            fill: false,
            borderColor: '#f87979',
            backgroundColor: '#FF3F3F',
            data: [
            ]
          },
          {
            label: 'FROM',
            fill: false,
            borderColor: '#23D323',
            backgroundColor: '#23D323',
            data: [
              {
                x: -2,
                y: -4
              },
              {
                x: -1,
                y: -1
              },
              {
                x: 0,
                y: 1
              },
              {
                x: 1,
                y: -1
              },
              {
                x: 2,
                y: -4
              }
            ]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        onClick: (e) => {
            const canvasPosition = ChartJS.helpers.getRelativePosition(e, chart);

            // Substitute the appropriate scale IDs
            const dataX = chart.scales.x.getValueForPixel(canvasPosition.x);
            const dataY = chart.scales.y.getValueForPixel(canvasPosition.y);
            console.log('Haaa')
        }
      }
    }
  }
}
</script>
