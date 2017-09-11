import { Component, OnInit } from '@angular/core';
import { TempRestService } from '../temp-rest.service';

@Component({
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
  skillPath = [
    {
      id: 1,
      name: 'Python',
      uri: '/pythonSkillTree',
      percentageCompleted: 20
    },
    {
      id: 2,
      name: 'HTML',
      uri: '/HTMLSkillTree',
      percentageCompleted: 45
    }
  ]
  id
  content: string[]
  data: JSON

  constructor(private service: TempRestService) { }


  ngOnInit() {
     this.service.getService().subscribe(data => {
      this.data = data;
      console.log(data);
      this.id = data['id'];
      this.content = data['content']
     });
  }



}
