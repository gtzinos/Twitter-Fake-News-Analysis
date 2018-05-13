import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AboutComponent } from './about.component';
import { RouterModule } from '@angular/router';
import {MatCardModule} from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

@NgModule({
  imports: [
    CommonModule,MatIconModule,MatCardModule, FormsModule, MatButtonModule,
    RouterModule.forChild([{path: '', component: AboutComponent}])
  ],
  declarations: [AboutComponent]
})
export class AboutModule { }
