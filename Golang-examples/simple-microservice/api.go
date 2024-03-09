package main

import (
	"context"
	"encoding/json"
	"net/http"
)

type ApiServer struct {
	svc Service
}

func NewApiServer(svc Service) *ApiServer {
	return &ApiServer{
		svc: svc,
	}
}
func (s *ApiServer) Start(listenaddr string) error {
	http.HandleFunc("/", s.handleGetFact)
	return http.ListenAndServe(listenaddr, nil)
}

func (s *ApiServer) handleGetFact(w http.ResponseWriter, r *http.Request) {
	fact, err := s.svc.GetCatFact(context.Background())
	if err != nil {
		writejson(w, http.StatusUnprocessableEntity, map[string]any{"error": err.Error()})
	}

	writejson(w, http.StatusOK, fact)
}

func writejson(w http.ResponseWriter, s int, v any) error {
	w.WriteHeader(s)
	w.Header().Add("content-type", "application/json")
	return json.NewEncoder(w).Encode(v)
}
