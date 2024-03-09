package main

import (
	"context"
	"encoding/json"
	"net/http"
)

type Service interface {
	GetCatFact(context.Context) (*CatFact, error)
}

type CatFactService struct {
	url string
}

func NewCatFactService(url string) Service {
	return &CatFactService{
		url: url,
	}

}
func (s *CatFactService) GetCatFact(cts context.Context) (*CatFact, error) {
	resp, err := http.Get(s.url)

	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	fact := &CatFact{}
	if err := json.NewDecoder(resp.Body).Decode((fact)); err != nil {
		return nil, err
	}
	return fact, nil

}
