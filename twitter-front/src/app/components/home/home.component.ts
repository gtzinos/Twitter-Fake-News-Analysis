import { RetweetsPerHop } from './../../shared/models/RetweetsPerHop';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { GraphsService } from '../../shared/services/graphs.service';
import { GraphConfiguration } from '../../shared/models/GraphConfiguration';
import { GraphDataConfiguration } from '../../shared/models/GraphDataConfiguration';
import { RetweetsPerMonth } from '../../shared/models/RetweetsPerMonth';
import { Users } from '../../shared/models/Users';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  public byDateGraph = [];
  public byHopGraph = [];
  public users = [];
  public selectedUser = undefined;
  public retweetsByDate = [];
  public retweetsByHop = [];

  constructor(public http: HttpClient, public graphService: GraphsService) { }

  ngOnInit() {
    this.http.get(environment.api + "/users").subscribe((users: [Users]) => {
      this.users = users;
    })
  }

  updateUser() {
    this.retweetsByDate = [];
    this.retweetsByHop = [];

    this.http.post(environment.api + "/retweets-per-month", { 'userId': this.selectedUser }).subscribe((retweetsByDate: [RetweetsPerMonth]) => {
      retweetsByDate.forEach(retweet => {
        let splitArray = retweet.id.split("/");
        retweet.id = splitArray[2] + "/" + splitArray[1] + "/" + splitArray[0];
      })
      this.byDateGraph.push(new GraphConfiguration("Retweets By Date", "line", new GraphDataConfiguration("count")));
      this.retweetsByDate = retweetsByDate;
    })

    this.http.post(environment.api + "/retweets-per-hop", { 'userId': this.selectedUser }).subscribe((retweetsByHop: [RetweetsPerHop]) => {
      this.byHopGraph.push(new GraphConfiguration("Retweets By Hop", "line", new GraphDataConfiguration("count")));
      this.retweetsByHop = retweetsByHop;
    })
  }
}
