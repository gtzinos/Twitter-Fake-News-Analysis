import { GraphDataConfiguration } from './GraphDataConfiguration';
export class GraphConfiguration {
  chartLabel: string;
  chartElement: CanvasRenderingContext2D;
  type: string;
  graphDataConfiguration: GraphDataConfiguration;

  constructor(chartLabel: string, type: string, graphDataConfiguration: GraphDataConfiguration,
     chartElement?: CanvasRenderingContext2D) {
      this.chartLabel = chartLabel;
      this.type = type;
      this.chartElement = chartElement || null;
      this.graphDataConfiguration = graphDataConfiguration;
    }
}
