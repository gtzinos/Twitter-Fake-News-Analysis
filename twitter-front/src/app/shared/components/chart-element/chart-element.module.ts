import { GraphsService } from './../../../shared/services/graphs.service';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ChartElementComponent } from './chart-element.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule, FormsModule
  ],
  declarations: [ChartElementComponent],
  providers: [GraphsService],
  exports: [ChartElementComponent]
})
export class ChartElementModule { }
