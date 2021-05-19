import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddnewarticleComponent } from './addnewarticle.component';

describe('AddnewarticleComponent', () => {
  let component: AddnewarticleComponent;
  let fixture: ComponentFixture<AddnewarticleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddnewarticleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddnewarticleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
