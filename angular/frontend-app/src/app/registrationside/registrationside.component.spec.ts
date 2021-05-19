import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistrationsideComponent } from './registrationside.component';

describe('RegistrationsideComponent', () => {
  let component: RegistrationsideComponent;
  let fixture: ComponentFixture<RegistrationsideComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistrationsideComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistrationsideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
