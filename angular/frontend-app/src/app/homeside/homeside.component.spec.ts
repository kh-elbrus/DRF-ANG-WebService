import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HomesideComponent } from './homeside.component';

describe('HomesideComponent', () => {
  let component: HomesideComponent;
  let fixture: ComponentFixture<HomesideComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HomesideComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HomesideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
