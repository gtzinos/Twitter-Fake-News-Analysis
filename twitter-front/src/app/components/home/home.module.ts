import { GraphsService } from './../../shared/services/graphs.service';
import { ChartElementModule } from './../../shared/components/chart-element/chart-element.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule,ChartElementModule,
    RouterModule.forChild([{path: '', component: HomeComponent}])
  ],
  declarations: [HomeComponent],
  providers: [GraphsService]
})
export class HomeModule { }
