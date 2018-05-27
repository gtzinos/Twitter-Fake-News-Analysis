import { GraphConfiguration } from './../../../shared/models/GraphConfiguration';
import { GraphsService } from './../../../shared/services/graphs.service';
import { ReviewPerYear } from './../../../shared/models/ReviewPerYear';
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit, Input, QueryList, ContentChildren, ViewChildren } from '@angular/core';
import { Chart } from 'chart.js';
import { environment } from '../../../../environments/environment';
import { RestaurantByWifi } from '../../../shared/models/RestaurantByWifi';
import { GraphDataConfiguration } from '../../../shared/models/GraphDataConfiguration';

@Component({
  selector: 'chart-element',
  templateUrl: './chart-element.component.html',
  styleUrls: ['./chart-element.component.css']
})
export class ChartElementComponent implements AfterViewInit {
  @Input() data;
  @Input() graphConfiguration: [GraphConfiguration];

  @ViewChildren("chartItem") chartItems: QueryList<any>;

  constructor(public graphService: GraphsService) { }

  ngAfterViewInit() {
    let colors = this.getColors(this.data.length);
    this.chartItems['_results'].forEach((chart, index) => {
      this.createGraph(chart, index, colors);
    });
  }


  getColors(length) {
    let colors = [];

    for (let i = 0; i < length; i++) {
      var letters = '0123456789ABCDEF';
      var color: string = '#';
      for (var j = 0; j < 6; j++) {
        color += letters[Math.floor(Math.random() * 16)];
      }

      colors.push(color);
    }

    return colors;
  }

  createGraph(chart, index: number, colors) {
    let chartItemCanvas = chart.nativeElement.getContext('2d');

    this.graphConfiguration[index].chartElement = chartItemCanvas;

    this.graphService.createChart(this.graphConfiguration[index], this.data, colors);
  }
}
