import { TestBed, inject } from '@angular/core/testing';

import { TempRestService } from './temp-rest.service';

describe('TempRestService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TempRestService]
    });
  });

  it('should be created', inject([TempRestService], (service: TempRestService) => {
    expect(service).toBeTruthy();
  }));
});
