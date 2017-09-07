import { Component, OnInit } from '@angular/core';
import { TempRestService } from '../temp-rest.service';

@Component({
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {

  id
  content: string[]
  data: JSON

  constructor(private service: TempRestService) { }


  ngOnInit() {
     this.service.getService().subscribe(data => {
      this.data = data;
      console.log(data);
      debugger;
      this.id = data['id'];
      this.content = data['content']
     });
  }

}
