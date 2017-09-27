import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SkillTreePopoverComponent } from './skill-tree-popover.component';

describe('SkillTreePopoverComponent', () => {
  let component: SkillTreePopoverComponent;
  let fixture: ComponentFixture<SkillTreePopoverComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SkillTreePopoverComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SkillTreePopoverComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
