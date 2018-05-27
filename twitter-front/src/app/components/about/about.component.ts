import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {


  developers = []
  constructor() { }

  ngOnInit() {
    let randomDevs = [{
      name: "Ilias Karatsin",
      title: "Full Stack Developer",
      photo: "https://scontent.fskg1-1.fna.fbcdn.net/v/t1.0-9/13226931_1233808183350275_6020287782455920427_n.jpg?_nc_cat=0&oh=78d74adeab14cb24b4af5997c6e7d9d6&oe=5B81C380",
      description: "Hello...",
      website: "",
      social: "",
      email: "mailto:karatsin@csd.auth.gr"
    },
    {
      name: "Anastasios Theodosiou",
      title: "Full Stack Developer",
      photo: "https://media.licdn.com/dms/image/C5103AQHN8Jvu3uDVZQ/profile-displayphoto-shrink_800_800/0?e=1531958400&v=beta&t=VSbVAqQTFYQxUBxGQchjFpDKXrxzU4TTFL-MCrPOXis",
      description: "Hello...",
      website: "https://about.me/anastasios.theodosiou",
      social: "https://www.linkedin.com/in/anastasios-theodosiou",
      email: "mailto:atheodos@csd.auth.gr"
    },
    {
      name: "Marinos Zagotsis",
      title: "Full Stack Developer",
      photo: "https://scontent.fskg1-1.fna.fbcdn.net/v/t1.0-9/13165870_10206152945047169_2926124721482332118_n.jpg?_nc_cat=0&oh=5fc8d7391a79a5699943be0ef1ee3812&oe=5B8C8D43",
      description: "Hello...",
      social: "https://gr.linkedin.com/in/marinoszagkotsis",
      email: "mailto:zagkotsis@csd.auth.gr"
    },
    {
      name: "George Tzinos",
      title: "Full Stack Developer",
      photo: "/assets/tzinos.png",
      description: "Hello...",
      website: "http://www.geotzinos.com",
      social: "https://www.linkedin.com/in/george-tzinos-8a6110101/",
      email: "mailto:gtzinosv@csd.auth.gr"
    }];

    for (var i = randomDevs.length - 1; i >= 0; i--) {
      this.developers.push(randomDevs.splice(randomDevs.length * Math.random() | 0, 1)[0]);
    }
  }

}
