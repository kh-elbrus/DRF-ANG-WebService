import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DialognotificationComponent } from './dialognotification.component';

describe('DialognotificationComponent', () => {
  let component: DialognotificationComponent;
  let fixture: ComponentFixture<DialognotificationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DialognotificationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DialognotificationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
