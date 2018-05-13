import { Routes, RouterModule } from '@angular/router';
import { ResponsiveTemplateComponent } from './responsive-template.component';


export const routes: Routes = [
 {
    path: '', component: ResponsiveTemplateComponent, children: [
      {
        path: '', redirectTo: 'home', pathMatch: 'full'
      },
      {
        path: 'home', loadChildren: '../../../components/home/home.module#HomeModule'
      },
      {
        path: 'about', loadChildren: '../../../components/about/about.module#AboutModule'
      }
    ]
  }
]
