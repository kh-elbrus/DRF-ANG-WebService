import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavPaginatorComponent } from './nav-paginator.component';

describe('NavPaginatorComponent', () => {
  let component: NavPaginatorComponent;
  let fixture: ComponentFixture<NavPaginatorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NavPaginatorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NavPaginatorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
