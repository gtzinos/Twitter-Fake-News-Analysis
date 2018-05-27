import { GraphsService } from './../../shared/services/graphs.service';
import { ChartElementModule } from './../../shared/components/chart-element/chart-element.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home.component';
import { RouterModule } from '@angular/router';
import { MatSelectModule } from '@angular/material';
import { FormsModule } from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,ChartElementModule,FormsModule,MatSelectModule,
    RouterModule.forChild([{path: '', component: HomeComponent}])
  ],
  declarations: [HomeComponent],
  providers: [GraphsService]
})
export class HomeModule { }
