import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SkillTreeConceptAdminApprovalComponent } from './skill-tree-concept-admin-approval.component';

describe('SkillTreeConceptAdminApprovalComponent', () => {
  let component: SkillTreeConceptAdminApprovalComponent;
  let fixture: ComponentFixture<SkillTreeConceptAdminApprovalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SkillTreeConceptAdminApprovalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SkillTreeConceptAdminApprovalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
