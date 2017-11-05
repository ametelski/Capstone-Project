import { Component, OnInit, Input } from '@angular/core';
import { ISkillConcept } from '../Models/skillConcept.model';
import { SkillpathService } from '../skillpath.service';

@Component({
  selector: 'app-skill-tree',
  templateUrl: './skill-tree.component.html',
  styleUrls: ['./skill-tree.component.css']
})
export class SkillTreeComponent implements OnInit {
  @Input() skillConcept: ISkillConcept[]


  // = {
  //   skillTitle: 'loops',
  //   skillDescriptionL: 'This module will go over loops',
  //   extLearnLinks: ['www.google.com'],
  //   completed: false
  // }
  constructor(private skill: SkillpathService) { }

  ngOnInit() {

  }

}
