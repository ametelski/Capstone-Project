import { TestBed, inject } from '@angular/core/testing';

import { SkillpathService } from './skillpath.service';

describe('SkillpathService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SkillpathService]
    });
  });

  it('should be created', inject([SkillpathService], (service: SkillpathService) => {
    expect(service).toBeTruthy();
  }));
});
