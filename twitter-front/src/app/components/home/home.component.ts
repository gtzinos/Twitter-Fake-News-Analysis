import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { GraphsService } from '../../shared/services/graphs.service';
import { GraphConfiguration } from '../../shared/models/GraphConfiguration';
import { GraphDataConfiguration } from '../../shared/models/GraphDataConfiguration';
import { RetweetsPerMonth } from '../../shared/models/RetweetsPerMonth';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  public graphConfigurations = [];
  public users = [];

  constructor(public http: HttpClient, public graphService: GraphsService) { }

  ngOnInit() {
    this.http.get(environment.api + "/retweets-per-month").subscribe((users: [RetweetsPerMonth]) => {

      this.graphConfigurations.push(new GraphConfiguration("Users By Year", "bar", new GraphDataConfiguration("count")));

      this.users = users;
    })
  }
}
