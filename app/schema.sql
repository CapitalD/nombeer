drop table if exists beers;
create table beers (
  id integer primary key autoincrement,
  name text not null,
  kegged_date integer,
  abv float,
  ibu integer 
);
