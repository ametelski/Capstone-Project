import { Component, OnInit, Input } from '@angular/core';
import { ISkillConcept } from '../Models/skillConcept.model';

@Component({
  selector: 'app-skill-tree-popover',
  templateUrl: './skill-tree-popover.component.html',
  styleUrls: ['./skill-tree-popover.component.css']
})
export class SkillTreePopoverComponent implements OnInit {
 @Input()popOver: ISkillConcept
  constructor() { }

  ngOnInit() {
  }

}
