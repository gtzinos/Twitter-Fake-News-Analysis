import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { RouterModule } from '@angular/router';
import { OverlayModule } from '@angular/cdk/overlay';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    HttpClientModule,
    OverlayModule,
    RouterModule.forRoot([{
      path: '', component: AppComponent, children: [
        {
          path: '', loadChildren: "./shared/components/responsive-template/responsive-template.module#ResponsiveTemplateModule"
        }
      ]
    }])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

